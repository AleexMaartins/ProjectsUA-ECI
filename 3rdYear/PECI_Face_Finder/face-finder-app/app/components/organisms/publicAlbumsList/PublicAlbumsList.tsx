"use client"
import { useEffect, useState } from "react";
import Text, { TextTypes } from "../../atoms/text/Text";
import AlbumCard from "../../molecules/albumCard/AlbumCard";
import { Album } from "@/src/constants/album";
import publicAlbumsListStyle from "./publicAlbumsListStyle.module.css";
import LoadingScreen from "../../molecules/loading/Loading";

export default function PublicAlbumsList(){
    const [albums, setAlbums] = useState<Album[]>([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(()=>{
        fetch('http://127.0.0.1:8000/albums')
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            setAlbums(data);
            setIsLoading(false);
        }).catch((error)=>{
            console.log(error)
            setIsLoading(false);
        })
    }, [])

    if (isLoading) {
        return <LoadingScreen />;
    }

    return (
        <div className={publicAlbumsListStyle.publicAlbumContainer}>
            <div>
                <Text 
                    text={"Discovery"}
                    type={TextTypes.HEADER}
                    color="main-blue"
                />
            </div>
            <div className={publicAlbumsListStyle.cards}>
                {
                    albums.map(album => {
                        return <AlbumCard 
                            id={album.id!} 
                            title={album.title}
                            ownerName={album.ownerName!}   
                            showLabel={false}         
                            thumbnail={album.thumbnail}        
                        />
                    })
                }
            </div>

        </div>
    );
}