'use client'
import Divider from "@/app/components/atoms/divider/Divider";
import StandardHeader from "@/app/components/molecules/standardHearder/StandardHeader";
import AlbumList from "@/app/components/organisms/album/AlbumOrganism";
import { getAuthHeaders } from "@/app/utils/requestHeader";
import dynamic from "next/dynamic";
import { usePathname } from "next/navigation";
import personStyle from './personPageSyle.module.css'
import { useEffect, useRef, useState } from "react";
import { IoMdArrowBack } from "react-icons/io";
import Text, { TextTypes } from "@/app/components/atoms/text/Text";
import { MdEdit } from "react-icons/md";
import Input from "@/app/components/atoms/input/Input";
import { FcCancel } from "react-icons/fc";
import { FaCheck } from "react-icons/fa";
import LoadingScreen from "@/app/components/molecules/loading/Loading";
import { LazyLoadImage } from 'react-lazy-load-image-component';
import personPageSyle from './personPageSyle.module.css'
import { get } from "http";


const Layout = dynamic(() => import('react-masonry-list'), {
    ssr: false,
  });
  
export default function PersonPage(){
    const pathName = usePathname()
    const [photos, setPhotos] = useState([])
    const [person, setPerson] = useState() 
    const [personLabel, setPersonLabel] = useState()
    const [isEditingLabel, setIsEditingLabel] = useState(false)
    const [isEditable, setIsEditable] = useState(false)
    const headers = getAuthHeaders()
    const [isLoading, setIsLoading] = useState(true)

    useEffect(()=>{

        const initialPersonLabel =  pathName.split("/")[4]
        fetch(`http://127.0.0.1:8000/photo/person/${initialPersonLabel}`, { headers })
        .then((res) => res.json())
        .then((data) => setPhotos(data))
        .catch((error)=> console.log(error))

        
        fetch(`http://127.0.0.1:8000/person/info/${initialPersonLabel}`, { headers })
        .then((res) => res.json())
        .then((data) => {
            setPerson(data)
            setIsLoading(false)
        }

        )
        .catch((error)=> {
            console.log(error)
            setIsLoading(false)    
        })
        checkEditPermissions()

    }, [])

    const handleLabelUpdate = () => {
        const data = {
            newLabel: personLabel, 
            oldLabel: person!.label
        }
        fetch(`http://127.0.0.1:8000/person/edit/`, {
            method:"POST", 
            body: JSON.stringify({newLabel: personLabel, oldLabel: person.label}),
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then((res) => {
            setIsEditingLabel(false)
            setPerson({...person, label: personLabel, is_named: true})
            return res.json();
        }).catch((error)=>{ 
            console.log(error)
        })
    }

    const checkEditPermissions = async () => {
        if (person) {
            const headers = getAuthHeaders()
            const albumId = pathName.split("/")[2];
            const response = await fetch(`http://127.0.0.1:8000/person/editPermissions/${albumId}`, { headers });
            const data = await response.json();
            if (data.message === "User has necessary permissions"){
                setIsEditable(true)
            }else{
                setIsEditable(false)
            }
        }
    }

    useEffect(()=>{
        if (person?.is_named && person?.label !==  pathName.split("/")[4] ){
            window.location.replace(`/albums/${pathName.split("/")[2]}/person/${person.label}`)
        }
        checkEditPermissions()
    }, [person])

    
    return (
        <div>
            {isLoading ? (
                <LoadingScreen/> // Display a loading screen when isLoading is true
            ) : (
                <div>
                    <div className={personStyle.header}>
                        <div style={{display:"flex"}}>
                            <IoMdArrowBack
                                cursor={"pointer"}
                                fontSize={"50px"}
                                color="#08263b"
                                onClick={()=>history.back()}
                            />

                            
                            <div className={personStyle.personLabelDiv}>
                                {
                                    !isEditingLabel ?
                                        <Text
                                            text={!person?.is_named ? "Unnamed" : person?.label} 
                                            type={TextTypes.HEADER}
                                            color="main-blue"
                                        /> 
                                    : <Input 
                                        name={"label"}
                                        placeholder={(!person?.is_named ? "Unnamed" : person?.label) ?? ""} 
                                        value={personLabel ?? ""} 
                                        onChange={({target}) => {
                                                setPersonLabel(target.value.trim().replace(/ /g, ''))
                                            }
                                        }
                                    />
                                }
                                <div className={personStyle.actionButtons}>
                                    {isEditingLabel &&  <FaCheck onClick={handleLabelUpdate}/>}
                                    {isEditable && !isEditingLabel && <MdEdit onClick={()=>setIsEditingLabel(true)}/>}
                                    {isEditingLabel &&  <FcCancel onClick={()=>setIsEditingLabel(false)} className={personStyle.cancelButton}/>}
                                </div>
                            </div>
                    </div>

                    <div className={personStyle.thumb}>
                        <img className={personStyle.thumb} src={person?.thumbnail_key ?? ""}/>
                    </div>
                    </div>


                    <Divider />

                    {/* Photos */}
                    <Layout
                        gap={5}
                        items={
                            photos.map((photo:any, index)=>{
                                return (
                                    <div key={index}>
                                        <LazyLoadImage 
                                       className={personPageSyle.photo} 
                                        src={photo.image_key} 
                                        alt="album"
                                        placeholder={<LoadingScreen option="option2"/>}
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
            )}
        </div>
    )
}