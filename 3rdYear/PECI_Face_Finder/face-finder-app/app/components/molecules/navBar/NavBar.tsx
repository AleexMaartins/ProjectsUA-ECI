"use client"
import React, { useState, useEffect } from 'react';
import Text, { TextTypes } from '../../atoms/text/Text'
import navBarStyle from './navBarStyle.module.css'
import { getAuthHeaders } from '../../../utils/requestHeader'
import cookies from 'js-cookie'
import LoadingScreen from '../loading/Loading';

export type NavBarProps = {
    isLogged?: boolean
    noLinks?: boolean
}

export default function NavBar({isLogged, noLinks}:NavBarProps){
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        setTimeout(() => {
            setIsLoading(false);
        }, 1500);
    }, []);

    const handleLogout = ()=>{
        cookies.remove('jwtToken');
        location.replace('/auth/logIn')
        
    }

    return(
        <div style={ !noLinks ? {position:"fixed"} : {}}>
            <div className={navBarStyle.auxBar}></div>
            <div className={`${navBarStyle.navContainer} ${noLinks ? navBarStyle.noLinks : navBarStyle.hasLinks }`}>
                <div onClick={()=>window.location.assign("/")} className={navBarStyle.logo}>
                    <Text 
                        text='Face' 
                        type={TextTypes.HEADER}
                        color='main-red'
                    />
                    <Text 
                        text='Findr.'  
                        type={TextTypes.HEADER}
                        color='main-blue'
                    />
                </div>
                {!noLinks &&
                    <div className={navBarStyle.authLinks}>
                {isLoading ? 
                    <Text text='Loading...' />
                    :
                    !isLogged ?
                        <>
                            <Text text='Login' link='/auth/logIn'/>
                            <Text text='Sign Up' link='/auth/signUp'/> 
                        </>
                        :  
                        <>
                            <Text text='Home' link='/'/>
                            <Text text='My albums' link='/albums'/> 

                            <div onClick={handleLogout}  >
                                <span className={navBarStyle.logout}> <Text text='Logout' /></span>
                            </div>
                        </>
                }
                    </div>
                }
            </div>
        </div>
    )
}