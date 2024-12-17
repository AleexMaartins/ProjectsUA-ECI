'use client'
import React, { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import fileUploadStyle from './fileUploadStyle.module.css'
import { ImFolderUpload } from 'react-icons/im';


export type FileUploadProps ={
    singleFile?: boolean
    onUpload:(acceptedFiles:any)=>void;
}
export default function FileUpload({onUpload, singleFile}: FileUploadProps){
    const { getRootProps, getInputProps } = useDropzone({
        accept: {
            'image/*': ['.jpeg', '.png']
        },
        onDrop: (acceptedFiles) => {
            onUpload(acceptedFiles);
        },
        multiple: singleFile != undefined ? !singleFile : undefined
    });

    const otherAtt = { directory: "", webkitdirectory: "" };

    return (
      <div {...getRootProps()} className={fileUploadStyle.dragArea} {...otherAtt}>
        <input {...getInputProps()}  />
        <ImFolderUpload style={{width:'50px', height:'50px'}} />
        <p>Drag and drop files here or click to browse.</p>
      </div>
    );
};
