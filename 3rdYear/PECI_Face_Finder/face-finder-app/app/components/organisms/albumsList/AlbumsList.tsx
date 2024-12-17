'use client'
import { ALBUM_VISIBILITY, Album } from "@/src/constants/album";
import Text, { TextTypes } from "../../atoms/text/Text";
import Button, { ButtonSize } from "../../atoms/button/Button";
import Divider from "../../atoms/divider/Divider";
import AlbumCard from "../../molecules/albumCard/AlbumCard";
import albumsListStyle from "./albumsListStyle.module.css"
import { useEffect, useState } from "react";
import Modal from "../../molecules/modal/Modal";
import CreateAlbumForm from "../createAlbumForm/CreateAlbumForm";
import FilterButton from "../../molecules/filterButton/FilterButton";
import StandardHeader from "../../molecules/standardHearder/StandardHeader";
import { IoFilter } from "react-icons/io5";
import Cookies from 'js-cookie';
import { getAuthHeaders } from "@/app/utils/requestHeader";
import React, { Suspense } from 'react';
import LoadingScreen from "../../molecules/loading/Loading";




const emptyNewAlbum: Album ={
    title: "",
    description:"",
    label:"",
    isPublic: false,
    thumbnail: ""
}
export default function AlbumsList(){
    const [uploadModalOpen, setUploadModalOpen] = useState(false)
    const [albums, setAlbums] = useState<Album[]>([])
    const LazyAlbumCard = React.lazy(() => import('../../molecules/albumCard/AlbumCard'));
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const headers = getAuthHeaders();
        console.log("Token for /albums/user:", headers.Authorization);
        fetch('http://127.0.0.1:8000/albums/user', { headers })
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            setAlbums(data);
            setIsLoading(false);
        }).catch((error)=>{
            console.log(error)
        })
    }, [])

    const handleNewAlbumSubmission = (event: any) => {
        event.preventDefault()
    
        const album = emptyNewAlbum;
        album.title = event.target.title.value
        album.description = event.target.description.value
        album.label = event.target.label.value
        album.isPublic = event.target.isPublic.checked
        
        const token = `Bearer ${Cookies.get('jwtToken')}`;
        console.log("Token for /albums:", token);
        fetch('http://127.0.0.1:8000/albums', {
            method:"POST", 
            headers: {
                'Content-Type': 'application/json',
                'Authorization': token
            },
            body: JSON.stringify(album)
        })
        .then((res) => {
            return res.json();
        })
        .then((data) => {
        window.location.assign(`albums/${data.id}`)
        }).catch((error)=>{
            console.log(error)
        })
    }

    return (
        <div>
            {/* Hearder */}
            <StandardHeader 
                title="My Albums"
                mainButtonText="New Album" 
                secondaryButtonIcon={<IoFilter/>}
                onClickMainButton={()=>setUploadModalOpen(true)} 
                onClickSecondaryButton={()=>{}}
            />

            <Divider />
            

            {/* Albums */}
            <div className={albumsListStyle.albumsContainer} style={{ position: 'relative' }}>
            {isLoading && (
                <div style={{
                    position: 'absolute',
                    top: 0,
                    left: 0,
                    right: 0,
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                }}>
            <LoadingScreen option="option1"/>
        </div>
    )}
    {albums.map(album => {
        return (
            <Suspense fallback={<LoadingScreen option="option2"/>}>
                <LazyAlbumCard 
                    key={album.id}
                    id={album.id!}
                    thumbnail={album.thumbnail}
                    showLabel
                    title={album.title}
                    label={album.label}
                />
            </Suspense>
        )
    })}
</div>

            {/* Modal */}
            {uploadModalOpen &&
                <Modal 
                    title="New Album" 
                    content=
                    {
                        <CreateAlbumForm
                            onCancel={()=>setUploadModalOpen(false)}
                            onSubmit={handleNewAlbumSubmission}
                        />
                    } 
                    onClose={()=>setUploadModalOpen(false)}
                />
            }
        </div>
    );
}

