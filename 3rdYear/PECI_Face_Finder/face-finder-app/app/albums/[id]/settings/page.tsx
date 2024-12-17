'use client'
import Input from "@/app/components/atoms/input/Input";
import settingsStyle from './settingsStyle.module.css'
import Text, { TextTypes } from "@/app/components/atoms/text/Text";
import { MdEdit } from "react-icons/md";
import Button, { ButtonSize, ButtonVariant } from "@/app/components/atoms/button/Button";
import { IoMdArrowBack } from "react-icons/io";
import Modal from "@/app/components/molecules/modal/Modal";
import { useEffect, useState } from "react";
import MultiEmailInput from "@/app/components/molecules/multiEmail/MultiEmailInput";
import { getAuthHeaders } from "@/app/utils/requestHeader";
import { usePathname } from "next/navigation";
import CreatePhotoModal from "../../../components/organisms/createPhotoModal/CreatePhotoModal";
import LoadingScreen from "@/app/components/molecules/loading/Loading";

export default function AlbumSettingsPage() {
    const pathName = usePathname();
    const [album, setAlbum] = useState(null);
    const [modalOpen, setModalOpen] = useState(false);
    const [collaborators, setCollaborators] = useState([]);
    const [emails, setEmails] = useState([]);
    const [role, setRole] = useState('participant');
    const headers = getAuthHeaders();
    const [uploadModalOpen, setUploadModalOpen] = useState(false)
    const [isLoading, setIsLoading] = useState(true);
    const [currentThumbnail, setCurrentThumbnail] = useState(null);

    useEffect(() => {
        fetchAlbumData();
        getCollaborators();
    }, []);

    const fetchAlbumData = () => {
        fetch(`http://127.0.0.1:8000/albums/${pathName.split("/")[2]}`, { headers })
            .then((res) => res.json())
            .then((data) => {
                console.log('Album data:', data);
                setAlbum(data);
                setCurrentThumbnail(data.thumbnail);
                setIsLoading(false);
            })
            .catch((error) => {
                console.error('Error fetching album data:', error);
                setIsLoading(false);
            });
    };

    const handleAddCollaborator = () => {
        const data = { emails, role };
        fetch(`http://127.0.0.1:8000/albums/${pathName.split("/")[2]}/permissions`, {
            method: "POST",
            body: JSON.stringify(data),
            headers
        })
            .then((res) => res.json())
            .then((data) => {
                console.log('Add collaborator response:', data);
                getCollaborators();
                setModalOpen(false);
            })
            .catch((error) => {
                console.error('Error adding collaborator:', error);
            });
    };

    const handlePhotoAddition = (files: File[]) => {
        const formData = new FormData();

        // Append files to form data
        [...files].forEach((file) => {
            formData.append("thumbnail", file);
        });

        // Update the album thumbnail on the backend
        fetch(`http://127.0.0.1:8000/albums/${pathName.split("/")[2]}/thumbnail`, {
            method: "PUT",
            body: formData,
            headers: {
                'Authorization': headers.Authorization
            }
        })
            .then((res) => {
                if (res.ok) {
                    // Optionally, handle successful response
                    setCurrentThumbnail(URL.createObjectURL(files[0]));
                    setUploadModalOpen(false);

                } else {
                    console.error("Failed to update album thumbnail");
                }
            })
            .catch((error) => {
                console.error('Error updating album thumbnail:', error);
            });
    }

    const getCollaborators = () => {
        fetch(`http://127.0.0.1:8000/albums/${pathName.split("/")[2]}/permissions`, { headers })
            .then((res) => res.json())
            .then((data) => {
                setCollaborators(data);
            })
            .catch((error) => {
                console.error('Error fetching collaborators:', error);
            });
    };

    return (
        isLoading ? <LoadingScreen /> : ( 
            <div className={settingsStyle.pageContainer}>
                <IoMdArrowBack
                    cursor="pointer"
                    fontSize="50px"
                    color="#08263b"
                    onClick={() => history.back()}
                />
                <div className={settingsStyle.block1}>
                    <div className={settingsStyle.thumb} onClick={() => setUploadModalOpen(true)}>
                        {currentThumbnail && (
                            <img
                                src={currentThumbnail}
                                alt="Album Thumbnail"
                                style={{ width: '100%', height: '100%', objectFit: 'cover', borderRadius: '16px', cursor: 'pointer'}}
                            />
                        )}
                        <MdEdit className={settingsStyle.editIcon} />
                    </div>
                    <div className={settingsStyle.inputsContainer}>
                        <Text text="Album settings" type={TextTypes.HEADER} color="main-blue" />
                        <Input name="title" placeholder={album?.title} disabled />
                        <Input name="description" placeholder={album?.description} disabled />
                        <Input name="label" placeholder={album?.label} disabled />
                        <div className={settingsStyle.block1Buttons}>
                            <div className={settingsStyle.checkboxContainer}>
                                <input type="checkbox" checked={album?.isPublic} disabled name="isPublic" style={{ width: "18px", height: "18px", cursor: "pointer" }} />
                                <Text text="This is a public album" />
                            </div>
                            <Button text="Add Collaborators" onClick={() => setModalOpen(true)} />
                        </div>
                    </div>
                </div>
                <div>
                    <Text text="Collaborators" type={TextTypes.HEADER} color="main-blue" />
                    <div className={settingsStyle.collaboratorsDiv}>
                        {collaborators.map(collaborator => (
                            <div key={collaborator.user_id}>
                                <Text text={`${collaborator.user_name}`} type={TextTypes.TEXT} color="main-blue" />
                                <Text text=" - " type={TextTypes.CAPTION} color="gray" />
                                <Text text={`${collaborator.role.toUpperCase()}`} type={TextTypes.CAPTION} color="gray" />
                            </div>
                        ))}
                    </div>
                </div>
                {modalOpen && (
                    <Modal
                        title="Add Collaborators"
                        content={
                            <div style={{ width: "100%" }}>
                                <div className={settingsStyle.emailsDiv}>
                                    <MultiEmailInput emails={emails} onChange={(event) => setEmails(event)} />
                                </div>
                                <div className={settingsStyle.selectRoleDiv}>
                                    <Text text="Role" type={TextTypes.SUBHEADER} color="main-blue" />
                                    <select required className={settingsStyle.selectField} onInput={(event) => setRole(event.target.value)}>
                                        <option value="participant">PARTICIPANT</option>
                                        <option value="photographer">PHOTOGRAPHER</option>
                                        <option value="admin">ADMIN</option>
                                    </select>
                                </div>
                                <div className={settingsStyle.footerButtons}>
                                    <Button
                                        text="Cancel"
                                        size={ButtonSize.MEDIUM}
                                        onClick={() => {
                                            setModalOpen(false);
                                            setEmails([]);
                                            setRole('participant');
                                        }}
                                    />
                                    <Button
                                        text="Add"
                                        variant={ButtonVariant.SAVE}
                                        size={ButtonSize.MEDIUM}
                                        type="submit"
                                        onClick={handleAddCollaborator}
                                    />
                                </div>
                            </div>
                        }
                        onClose={() => setModalOpen(false)}
                    />
                )}
                {uploadModalOpen &&
                    <CreatePhotoModal
                        title="Add Photos"
                        search={false}
                        confirmButtonText="Save"
                        onClose={() => setUploadModalOpen(false)}
                        onSubmit={handlePhotoAddition}
                    />
                }

            </div>
        )
    );

}
