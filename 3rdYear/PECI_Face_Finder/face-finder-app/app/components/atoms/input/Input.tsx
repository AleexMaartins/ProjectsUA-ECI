"use client"
import { ReactNode, useState } from 'react';
import inputStyle from './inputStyle.module.css'
import { AiFillEye, AiFillEyeInvisible } from "react-icons/ai";

export type InputProps={
    name:string;
    value?:string;
    placeholder?:string;
    type?:string;
    width?:string;
    icon?:ReactNode;
    required?:boolean;
    disabled?: boolean;
    onChange?: (params:any) => void;
}

export default function Input(
    {
    name, 
    value,
    placeholder, 
    type="text", 
    width, 
    icon,
    disabled,
    required, 
    onChange,
}:InputProps){

    const inputClasses = ()=>{
        return `${inputStyle.baseInput}`
    }
    const inputContainerClasses =()=>{
        return `${inputStyle.inputContainer} ${!width && inputStyle.fullWidth}`
    }

    return (
        <div className={inputContainerClasses()} style={{width:width}}>
            <input
                disabled={disabled}
                name={name}
                value={value}
                className={inputClasses()}
                placeholder={placeholder}
                type={type}
                required={required}
                onChange={onChange ? onChange: undefined}
            />
            {icon}
        </div>
        
    );

}