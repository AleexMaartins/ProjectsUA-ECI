'use client'
import Button, { ButtonSize } from "@/app/components/atoms/button/Button";
import Input from "@/app/components/atoms/input/Input";
import forgotStyle from "./forgotStyle.module.css";
import baseAuthStyle from "../baseAuthStyle.module.css"
import Text, { TextTypes } from "@/app/components/atoms/text/Text";
import { AiFillEye, AiFillEyeInvisible } from "react-icons/ai";
import { FormEvent, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";

export default function forgot(){

    const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const formData = new FormData(event.target as HTMLFormElement);
        const email = formData.get('email');
        console.log(email);
     
        const response = await fetch('http://127.0.0.1:8000/auth/forgot', { //check if email exists on database
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email })
        });
    
        if (response.ok) {
            console.log('Email exists, sending email with instructions to reset password');            
        } else {
            const data = await response.json();
            if (data.error === "This user does not exist") {
                alert("This user does not exist");
            } else {
                console.error('Error finding user email');
            }
        }
    }
    return (
        <div className={baseAuthStyle.pageContainer} >

            <form className={baseAuthStyle.formContainer} method="post" onSubmit={handleSubmit}>
                <Text text="< Log In" type={TextTypes.CAPTION} link="logIn"/>
                <Text text="Forgot Password"  type={TextTypes.HEADER}/>
                <Text text="You will be sent an email with more information "  type={TextTypes.TEXT}/>

                <div className={baseAuthStyle.inputs}>
                    <Input placeholder="Email" name="email" required/>             
                </div>

                <Button text="Submit" type="submit" size={ButtonSize.FULL}/>

                <div className={forgotStyle.createAccountDiv}>
                    <Text text="Don't have an account?" type={TextTypes.CAPTION} />
                    <Text text="Create an account" type={TextTypes.CAPTION} link="signUp"/>
                </div>

            </form>
            
        </div>

    );
}