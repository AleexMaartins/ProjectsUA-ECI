'use client'
import Button, { ButtonSize, ButtonVariant } from "@/app/components/atoms/button/Button";
import Input from "@/app/components/atoms/input/Input";
import signUpStyle from "./signUpStyle.module.css"
import baseAuthStyle from "../baseAuthStyle.module.css"
import Text, { TextTypes } from "@/app/components/atoms/text/Text";
import { AiFillEye, AiFillEyeInvisible } from "react-icons/ai";
import { FormEvent, useState } from "react";
import Link from "next/link";
export default function SignUp(){
    const [showPassword, setShowPassword] = useState(false);
    const [passwordError, setPasswordError] = useState('');
    const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const formData = new FormData(event.target as HTMLFormElement);
        const email = formData.get('email');
        const password = formData.get('password');
        const name = formData.get('text');
        
        const response = await fetch('http://127.0.0.1:8000/auth/sign-up', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password, name })
        });

        if (response.ok) {
            console.log('User created sucessfully');            
            window.location.replace("/auth/logIn")
        } else if (response.status === 400) {
            setPasswordError("Password should be at least 6 characters.");
        } else {
            const data = await response.json();
            if (data.error === "A user with this email already exists") {
                alert("A user with this email already exists");
            } else {
                console.error('Error creating user');
            }
        }

    }


    return (
        <div className={baseAuthStyle.pageContainer}>
            <form className={baseAuthStyle.formContainer} method="post" onSubmit={handleSubmit}>
                <div className={signUpStyle.headersContainer}>
                    <Text text="Create an account"  type={TextTypes.HEADER}/>
                    <Text text="Let's get started!"  />
                </div>

                <div className={baseAuthStyle.inputs}>
                    <Input placeholder="Name" name="text" required/>
                    <Input placeholder="Email" name="email" required/>
                    <Input 
                        placeholder="Password" 
                        name="password" 
                        type={showPassword?"text": "password"} 
                        required
                        icon={
                            showPassword?
                            <AiFillEye 
                                className={signUpStyle.passIcon}
                                onClick={()=>setShowPassword(!showPassword)}
                            />
                            :
                            <AiFillEyeInvisible 
                                className={signUpStyle.passIcon}
                                onClick={()=>setShowPassword(!showPassword)}
                            />
                        }
                    />
                    {passwordError && <div style={{color: 'red'}}>{passwordError}</div>}
                </div>  
                <div>
                    <div className={signUpStyle.buttonsContainer}>
                        <Button text="Sign up" type="submit" size={ButtonSize.FULL}/>
                    </div>
                    <div style={{marginTop:"10px", display:"flex", gap:"5px"}}>
                        <Text text="Already have an account?" type={TextTypes.CAPTION} />
                        <Text link="./logIn" text="Log in" type={TextTypes.CAPTION}/> 
                    </div>
                </div>

            </form>
            
        </div>

    );
}