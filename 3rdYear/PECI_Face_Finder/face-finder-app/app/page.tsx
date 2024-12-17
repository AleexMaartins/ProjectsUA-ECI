'use client'
import Cookies from 'js-cookie';
import NavBar from "./components/molecules/navBar/NavBar";
import PublicAlbumsList from "./components/organisms/publicAlbumsList/PublicAlbumsList";
import { useEffect } from 'react';
import { useState } from 'react';
import { getAuthHeaders } from './utils/requestHeader';


export default function HomePage(){
    const [isLogged, setIsLogged] = useState(false);

    useEffect(()=>{
      const headers = getAuthHeaders();
        
      fetch(`http://127.0.0.1:8000/auth/userInfo`, { headers })
      .then((res) => {
          if(!res.ok){
            throw new Error("Error in request")
          }
          setIsLogged(true)
      }).catch((error)=>{
          console.log(error)
      })
    },[])

    return (
      <div>
        
        <div>
          <NavBar isLogged={isLogged}/>
        </div>

        <div style={{padding:"150px 70px 100px 70px"}}>
          <PublicAlbumsList />
        </div> 

      </div>
     
    );
}