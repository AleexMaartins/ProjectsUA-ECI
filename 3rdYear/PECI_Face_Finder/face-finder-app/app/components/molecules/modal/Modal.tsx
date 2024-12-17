import { ReactNode } from 'react';
import Text, { TextTypes } from '../../atoms/text/Text';
import modalStyle from './modalStyle.module.css'
import Button, { ButtonSize, ButtonVariant } from '../../atoms/button/Button';
import { IoIosClose } from 'react-icons/io';

export type ModalProps = {
    title:string
    description?: string
    content: ReactNode
    onClose:()=>void
}

export default function Modal({title, description, content, onClose}:ModalProps){
    return(
        <div className={modalStyle.modalPannel} >
            <div className={modalStyle.modalContainer}>
                <IoIosClose 
                    className={modalStyle.closeModal} 
                    style={{width:'40px', height:'40px'}} 
                    onClick={onClose}
                />

                <div className={modalStyle.modalHeader}>
                    <Text text={title} type={TextTypes.HEADER} color='#08263b'/>
                    <Text text={description??""}/>
                </div>

                <div className={modalStyle.modalContent}>
                    {content}
                </div>       
            </div>
        </div>
        
    );
}