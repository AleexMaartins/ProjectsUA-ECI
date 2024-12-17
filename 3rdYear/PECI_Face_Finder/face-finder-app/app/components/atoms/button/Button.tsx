import buttonStyle from './buttonStyle.module.css'
import { ReactNode } from "react";


type ButtonProps={
    text?: string;
    onClick?: () => void;
    size?: ButtonSize;
    variant?: ButtonVariant;
    icon?: ReactNode;
    type?: ("submit" | "reset" | "button")
}

export enum ButtonSize {
    SMALL, 
    MEDIUM, 
    BIG, 
    FULL, 
}

export enum ButtonVariant {
    CONTAINED, 
    OUTLINED, 
    SAVE,
}

export default function Button({
    text, 
    onClick,
    size = ButtonSize.BIG, 
    variant= ButtonVariant.CONTAINED, 
    icon, 
    type
    }:ButtonProps){


    const btnSize =()=>{
        switch (size) {
            case ButtonSize.SMALL:
                return buttonStyle.btnSmall;
            case ButtonSize.MEDIUM:
                return buttonStyle.btnMedium;
            case ButtonSize.FULL:
                return buttonStyle.btnFull;
            default:
                return buttonStyle.btnBig;
        }
    }

    const btnVariant =()=>{
        switch (variant) {
            case ButtonVariant.CONTAINED:
                return buttonStyle.btnContained;
            case ButtonVariant.SAVE:
                return buttonStyle.btnSave;
            default:
                return buttonStyle.btnOutlined;
        }
    }

    const buttonClasses =()=>{
        const sizeClass = btnSize();
        const variantClass = btnVariant();
    
        return `${buttonStyle.btnBase} ${sizeClass} ${variantClass}`
    }

    return (
        <button 
            onClick={onClick}
            className={buttonClasses()}
            type= {type}
        >
            {text}
            {icon}
        </button>
    );
}