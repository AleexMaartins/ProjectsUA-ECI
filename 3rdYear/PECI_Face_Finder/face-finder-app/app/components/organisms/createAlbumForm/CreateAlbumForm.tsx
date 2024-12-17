import { useState } from "react";
import createAlbumStyle from "./createAlbumStyle.module.css"
import Input from "../../atoms/input/Input";
import Text from "../../atoms/text/Text";
import Button, { ButtonSize, ButtonVariant } from "../../atoms/button/Button";


export type CreateAlbumForm = {
    onCancel:()=>void
    onSubmit:(params:any)=>void
}

export default function CreateAlbumForm({onCancel, onSubmit}: CreateAlbumForm){
    return(
        <form className={createAlbumStyle.createForm} onSubmit={onSubmit} method="POST">
            <Input name="title" placeholder="Album Title"/>
            <Input name="description" placeholder="Description"/>
            <Input name="label" placeholder="Label"/>
            <div className={createAlbumStyle.checkboxContainer}>
                <input type="checkbox" name="isPublic" className={createAlbumStyle.checkbox}/>
                <Text text="This is a public album"/>
            </div> 
            <div className={createAlbumStyle.formFooter}>
                <Button 
                    text='Cancel' 
                    size={ButtonSize.MEDIUM} 
                    onClick={onCancel}
                />
                <Button 
                    text='Save' 
                    variant={ButtonVariant.SAVE} 
                    size={ButtonSize.MEDIUM}
                    type="submit"
                />
            </div>
     
        </form>
    );
}