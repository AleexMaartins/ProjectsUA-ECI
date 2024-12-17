'use client'

import Text, { TextTypes } from "@/app/components/atoms/text/Text";
import { IoFilter, IoSettingsOutline } from "react-icons/io5";
import { MdHeight, MdOutlineCloudUpload } from "react-icons/md";
import albumListStyle from './albumListStyle.module.css'
import Divider from "@/app/components/atoms/divider/Divider";
import { useEffect, useState } from "react";
import { Album } from "@/src/constants/album";
import CreatePhotoModal from "../createPhotoModal/CreatePhotoModal";
import { PersonCard } from "../../molecules/personCard/PersonCard";
import { getAuthHeaders } from "@/app/utils/requestHeader";
import dynamic from 'next/dynamic';
import StandardHeader from "../../molecules/standardHearder/StandardHeader";
import Button, { ButtonSize, ButtonVariant } from "../../atoms/button/Button";
import Modal from "../../molecules/modal/Modal";
import { usePathname } from "next/navigation";
import { LazyLoadImage } from 'react-lazy-load-image-component';
import LoadingScreen from "../../molecules/loading/Loading";
import React, { Suspense } from 'react';


const Layout = dynamic(() => import('react-masonry-list'), {
    ssr: false,
});

export type AlbumListProps = {
    albumId: string
}
const headers = getAuthHeaders();


export default function AlbumOrganism({ albumId }: AlbumListProps) {
    const [album, setAlbum] = useState<Album>()
    const [photos, setPhotos] = useState([])
    const [uploadModalOpen, setUploadModalOpen] = useState(false)
    const [searchModalOpen, setSearchModalOpen] = useState(false)
    const [photoActionsModalOpen, setPhotoActionsModalOpen] = useState(false)
    const [persons, setPersons] = useState([]);
    const [searchResult, setSearchResult] = useState([]);
    const [hasUploadPermission, setHasUploadPermission] = useState(false);
    const [hasSettingsPermission, setHasSettingsPermission] = useState(false);
    const pathName = usePathname()
    const [isLoading, setIsLoading] = useState(true);
    const [isUnauthorized, setIsUnauthorized] = useState(false);
    const [selectedPhoto, setSelectedPhoto] = useState(null);

    useEffect(() => {
        const headers = getAuthHeaders();
        fetch(`http://127.0.0.1:8000/albums/${albumId}`, { headers })
            .then((res) => {
                if (res.status === 401) {
                    setIsUnauthorized(true);
                    throw new Error('Unauthorized');
                }
                return res.json();
            })
            .then((data) => {
                setAlbum(data);
                // setIsLoading(false);
            }).catch((error) => {
                console.log(error)
            })

        fetch(`http://127.0.0.1:8000/person/${albumId}`, { headers })
            .then((res) => {
                if (res.status === 401) {
                    setIsUnauthorized(true);
                    throw new Error('Unauthorized');
                }
                return res.json();
            })
            .then((data) => {
                setPersons(data);
            }).catch((error) => {
                console.log(error)
            })

        loadPhotos();
        checkUploadPermissions();
        checkSettingsPermissions();
    }, []);

    const handlePhotoAddition = (files: File[]) => {
        const formData = new FormData();

        [...files].forEach((file) => {
            formData.append("files", file);
        });

        const headers = getAuthHeaders();
        fetch(`http://127.0.0.1:8000/photo/${albumId}`, {
            method: "POST",
            body: formData,
            headers
        })
            .then((res) => {
                if (res.status === 401) {
                    setIsUnauthorized(true);
                    throw new Error('Unauthorized');
                }
                setUploadModalOpen(false)
                loadPhotos()
                return res.json();
            }).catch((error) => {
                console.log(error)
            })
    }

    const loadPhotos = () => {
        const headers = getAuthHeaders();
        fetch(`http://127.0.0.1:8000/photo/${albumId}`, { headers })
            .then((res) => {
                if (res.status === 401) {
                    setIsUnauthorized(true);
                    throw new Error('Unauthorized');
                }
                return res.json();
            })
            .then((data) => {
                setPhotos(data);
            }).catch((error) => {
                console.log(error)
            })
    }

    const handleSearch = (files: File[]) => {
        const headers = getAuthHeaders();
        const formData = new FormData();

        formData.append("file", files[0]);

        fetch(`http://127.0.0.1:8000/photo/search/${albumId}`, {
            method: "POST",
            body: formData,
            headers
        })
            .then((res) => res.json())
            .then(res => {
                setSearchResult(res)
                setSearchModalOpen(false)
            })
            .catch((error) => {
                console.log(error)
            })
    }

    const checkUploadPermissions = async () => {
        const headers = getAuthHeaders();
        const response = await fetch(`http://127.0.0.1:8000/albums/upload/${albumId}`, { headers });
        const data = await response.json();
        if (data.message === "User has necessary permissions") {
            setHasUploadPermission(true);
            setIsLoading(false);
        } else {
            setHasUploadPermission(false);
            setIsLoading(false);
        }
    }

    const checkSettingsPermissions = async () => {
        const headers = getAuthHeaders();
        const response = await fetch(`http://127.0.0.1:8000/albums/settings/${albumId}`, { headers });
        const data = await response.json();
        if (data.message === "User has necessary permissions") {
            setHasSettingsPermission(true);
        } else {
            setHasSettingsPermission(false);
        }
    }

    if (isLoading) {
        return <LoadingScreen option="option1" />;
    }

    if (isUnauthorized) {
        return <div style={{ color: 'red' }}>You do not have access to this album.</div>;
    }

    const handleOpenPhotoActionsModal = (id) => {
        const photo = photos.find((photo) => photo.id === id);
        setPhotoActionsModalOpen(true);
        setSelectedPhoto(photo);
    }

    const downloadImage = async (photoId: string) => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/photo/download/${photoId}`, { headers });
            const blob = await response.blob();

            if (!blob) {
                throw new Error('Blob is undefined');
            }

            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = `${photoId}.jpg`;
            link.click();
            window.URL.revokeObjectURL(url);
        } catch (error) {
            console.error('Error downloading image:', error);
        }
    };

    const handleDeletePhoto = (photoId: string) => {
        fetch(`http://127.0.0.1:8000/photo/${photoId}`, {
            method: 'DELETE',
            headers
        })
            .then((res) => {
                if (!res.ok) {
                    throw new Error(res.statusText);
                }
                return res.json();
            })
            .then((data) => {
                window.location.assign(`/albums/${albumId}`);
            })
            .catch((error) => {
                console.error('Error deleting photo:', error);
            });
    };
    return (
        <div>
            {/* Header */}
            <StandardHeader
                title={album?.title!}
                mainButtonText={hasUploadPermission ? "Upload" : ""}
                mainButtonIcon={hasSettingsPermission ? <IoSettingsOutline /> : null}
                arrowBack={searchResult.length > 0}
                onClickArrowButton={() => setSearchResult([])}
                hasRigthButtons={searchResult.length == 0}
                secondaryButtonIcon={<MdOutlineCloudUpload />}
                additionalButton={
                    <Button 
                        text={"Search"}
                        size={ButtonSize.BIG}
                        variant={ButtonVariant.OUTLINED}
                        onClick={() => setSearchModalOpen(true)}
                    />
                }
                onClickMainButton={hasUploadPermission ? () => setUploadModalOpen(true) : undefined}
                onClickSecondaryButton={() => location.assign(`${pathName}/settings`)}
            />

            <Divider />
            {
                !(searchResult.length > 0) ?
                    <div>
                        {/* People */}
                        <div className={albumListStyle.peopleSection}>
                            {
                                persons.length > 7 &&
                                <div className={albumListStyle.showAllCaption}>
                                    <Text
                                        text={"Show all people"}
                                        type={TextTypes.CAPTION}
                                        link={`${album?.id}/people`}
                                    />
                                </div>
                            }

                            <div className={albumListStyle.personCards}>
                                {persons.map((person: any, index) => {
                                    return (
                                        <PersonCard
                                            key={index}
                                            person={person.is_named ? person.label : "Unnamed"}
                                            onClick={() => location.assign(`/albums/${albumId}/person/${person.label}`)}
                                            thumbnail={person.thumbnail_key}
                                        />
                                    )
                                })}
                            </div>
                        </div>

                        {/* Photos */}
                        <Layout
                            gap={5}
                            items={
                                photos.map((photo: any, index) => {
                                    return (
                                        <div key={index}
                                            onClick={() => handleOpenPhotoActionsModal(photo.id)}>
                                            <LazyLoadImage
                                                className={albumListStyle.photo}
                                                src={photo.image_key}
                                                alt="album"
                                                placeholder={<LoadingScreen option="option2" />}
                                                // height={'100%'}
                                                // width={'100%'}
                                                onLoad={() => { // Force a re-render of the grid
                                                    setPhotos([...photos]);
                                                }}
                                            />
                                        </div>
                                    )
                                })
                            }
                        />
                    </div>
                    :
                    <div>
                        {/* Search */}
                        <Layout
                            gap={5}
                            items={
                                searchResult.map((photo: any, index) => {
                                    return (
                                        <div key={index}
                                            onClick={() => location.assign(`/albums/${albumId}/photo-details/${photo.id}`)}>
                                            <LazyLoadImage
                                                className={albumListStyle.photo}
                                                src={photo.image_key}
                                                alt="album"
                                                placeholder={<LoadingScreen option="option2" />}
                                                // height={'100%'}
                                                // width={'100%'}
                                                onLoad={() => { // Force a re-render of the grid
                                                    setPhotos([...photos]);
                                                }}
                                            />
                                        </div>
                                    )
                                })
                            }
                        />
                    </div>

            }


            {
                uploadModalOpen &&
                <CreatePhotoModal
                    title="Add Photos"
                    search={false}
                    confirmButtonText="Save"
                    onClose={() => setUploadModalOpen(false)}
                    onSubmit={handlePhotoAddition}
                />
            }
            {
                searchModalOpen &&
                <CreatePhotoModal
                    title="Search Face"
                    search={true}
                    description="Insert a photo with that one face you are looking for"
                    confirmButtonText="Search"
                    onClose={() => setSearchModalOpen(false)}
                    onSubmit={handleSearch} />
            }
            {
                photoActionsModalOpen &&
                <Modal
                    title="Photo Actions"
                    description="Download photo"
                    onClose={() => setPhotoActionsModalOpen(false)}
                    content={
                        <div style={{ width: "100%" }}>
                            <div style={{ display: "flex", justifyContent: "center" }}>
                                <img src={selectedPhoto.image_key} alt="" style={{ width: "50%" }} />
                            </div>
                            <div style={{ display: "flex", justifyContent: "flex-end", padding: "1rem", columnGap: "1rem" }} >
                                <Button
                                    text={"Download"}
                                    variant={ButtonVariant.SAVE}
                                    size={ButtonSize.MEDIUM}
                                    type="submit"
                                    onClick={() => downloadImage(selectedPhoto.id)}
                                />
                            </div>
                        </div>
                    }
                />
            }
        </div >
    );
}