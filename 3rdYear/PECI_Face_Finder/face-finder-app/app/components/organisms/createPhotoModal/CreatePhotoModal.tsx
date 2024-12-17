'use client'
import { useState } from "react";
import Button, { ButtonSize, ButtonVariant } from "../../atoms/button/Button";
import FileUpload from "../../molecules/fileUpload/fileUpload";
import createPhotoModalStyle from './createPhotoModalStyle.module.css'
import Text from "../../atoms/text/Text";
import { IoIosClose } from "react-icons/io";
import Modal from "../../molecules/modal/Modal";
import LoadingScreen from "../../molecules/loading/Loading";

export type CreatePhotoModalProps = {
    title: string
    description?: string
    confirmButtonText: string
    search?:boolean,
    onClose:()=>void,
    onSubmit:(files:File[])=>void
}
export default function CreatePhotoModal({title, description, search, confirmButtonText, onClose, onSubmit}: CreatePhotoModalProps){
    const [uploadedFiles, setUploadedFiles] = useState([]);
    const [isLoading, setIsLoading] = useState(false);


    const removeFile = (name:string) => {
        setUploadedFiles(uploadedFiles.filter((file: File) =>  file.name !== name))
    }

    return (
        <Modal 
            title={title}
            onClose={onClose}
            description={description}
            content=
            {
                <div style={{width: '100%', height: '100%'}}>
                    <div className={createPhotoModalStyle.photoModalContainer}>
                        {isLoading ? 
                            <div style={{position: 'absolute', left: 0, right: 0, bottom: 0}}>
                                <LoadingScreen />
                            </div>
                            : 
                            <>
                                <div className={createPhotoModalStyle.list}>
                                    {
                                        !uploadedFiles.length ? 
                                            <div className={createPhotoModalStyle.dropZone}>
                                                <FileUpload singleFile={search??undefined} onUpload={(files)=>setUploadedFiles(files)}/>
                                            </div>
                                        : 
                                            <div className={createPhotoModalStyle.fileList} >
                                                {uploadedFiles.map((file: File) => {
                                                    return search ?
                                                            <div
                                                            style={{
                                                                backgroundImage: `url(${URL.createObjectURL(file)})`,
                                                                width: "100%",
                                                                height: "100%", 
                                                                backgroundPosition: "center", 
                                                                backgroundSize: 'contain',
                                                                backgroundRepeat: 'no-repeat'
                                                            }}
                                                            >
                                                        
                                                            </div>
                                                            : <div className={createPhotoModalStyle.listedFile} key={file.name}>
                                                                <Text text={file.name}/>
                                                                <IoIosClose 
                                                                    style={{width:'20px', height:'20px', cursor:'pointer'}} 
                                                                    onClick={() => removeFile(file.name)}
                                                                />
                                                            </div>
                                                        
                                                })}
                                            </div>
                                    }
                                </div>
                                <div className={createPhotoModalStyle.footerButtons}>
                                    <Button 
                                        text='Cancel' 
                                        size={ButtonSize.MEDIUM} 
                                        onClick={onClose}
                                    />
                                    <Button 
                                        text={confirmButtonText} 
                                        variant={ButtonVariant.SAVE} 
                                        size={ButtonSize.MEDIUM}
                                        type="submit"
                                        onClick={async () => {
                                            setIsLoading(true);
                                            await onSubmit(uploadedFiles);
                                        }}
                                    />
                                </div>
                            </>
                        }
                    </div>
                </div>
            }
        />
    );
}