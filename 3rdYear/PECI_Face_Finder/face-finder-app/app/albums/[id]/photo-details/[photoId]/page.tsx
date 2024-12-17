'use client'
import { getAuthHeaders } from "@/app/utils/requestHeader";
import { useEffect, useState } from "react";
import { IoMdArrowBack, IoMdDownload, IoMdTrash } from "react-icons/io";
import settingsStyle from './settingsStyle.module.css'
import Button, { ButtonSize, ButtonVariant } from "@/app/components/atoms/button/Button";
import { usePathname } from "next/navigation";
export default function PhotoSettingsPage() {
    const [photo, setPhoto] = useState(null);
    const [albumId, setAlbumId] = useState<string | null>(null);
    const [photoId, setPhotoId] = useState<string | null>(null);
    const headers = getAuthHeaders();
    const pathName = usePathname();

    useEffect(() => {
        const albumIdFromPath = pathName.split("/")[2];
        const photoIdFromPath = pathName.split("/")[4];
        setAlbumId(albumIdFromPath);
        setPhotoId(photoIdFromPath);
        fetchPhotoData(albumIdFromPath, photoIdFromPath);
    }, []);

    const fetchPhotoData = (albumId: string, photoId: string) => {
        fetch(`http://127.0.0.1:8000/photo/${albumId}/details/${photoId}`, { headers })
            .then((res) => res.json())
            .then((data) => {
                setPhoto(data);
            })
            .catch((error) => {
                console.error('Error fetching photo data:', error);
            });
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

    return (
        <div className={settingsStyle.pageContainer}>
            <IoMdArrowBack
                cursor="pointer"
                fontSize="50px"
                color="#08263b"
                onClick={() => history.back()}
            />
            <div className={settingsStyle.photoAndButtons}>
                <div>
                    {photo?.image_key && (
                        <img
                            className={settingsStyle.photo} 
                            src={photo.image_key}
                            alt="Photo"
                        />
                    )}
                </div>
                <div className={settingsStyle.block1Buttons}>
                    <Button text="Delete Photo" onClick={() => {
                        if (photoId) {
                            handleDeletePhoto(photoId);
                        }
                    }} />
                    <Button text="Download Photo" onClick={() => {
                        if (photoId) {
                            downloadImage(photoId);
                        }
                    }} />
                </div>
            </div>
        </div>
    );
}