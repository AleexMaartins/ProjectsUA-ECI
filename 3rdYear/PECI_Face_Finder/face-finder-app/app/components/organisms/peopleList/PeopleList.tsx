'use client'
import Text, { TextTypes } from "../../atoms/text/Text";
import peopleListStyle from './peopleListStyle.module.css'
// import { PersonCard } from "../../molecules/personCard/PersonCard";
import { useEffect, useState } from "react";
import { getAuthHeaders } from "@/app/utils/requestHeader";
import { usePathname } from "next/navigation";
import StandardHeader from "../../molecules/standardHearder/StandardHeader";
import LoadingScreen from "../../molecules/loading/Loading";
import {lazy, Suspense} from 'react';

const LazyPersonCard = lazy(() => import('../../molecules/personCard/PersonCard').then(module => ({ default: module.PersonCard })));

export default function PeopleList(){
    const [people, setPeople] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const pathName = usePathname()

    useEffect(()=>{
        const headers = getAuthHeaders();
        
        fetch(`http://127.0.0.1:8000/person/${pathName.split("/")[2]}`, { headers })
        .then((res) => {
            return res.json();
        })
        .then((data) => {
            setPeople(data);
            setIsLoading(false);
        }).catch((error)=>{
            console.log(error)
            setIsLoading(false);
        })
    }, [])

    if (isLoading) {
        return <LoadingScreen />;
    }

    return (
        <div>
            <StandardHeader 
                title={"All people"}
                arrowBack={true}
                hasRigthButtons={false}
            />
            <div className={peopleListStyle.peopleListDiv}>
                <Suspense fallback={<LoadingScreen option="option2"/>}>
                    {
                        people.map((person:any, index) => {
                            return (
                                <LazyPersonCard
                                    key={index}
                                    person={person.is_named ? person.label : "Unnamed"}
                                    thumbnail={person.thumbnail_key}
                                    onClick={()=>location.assign(`/albums/${pathName.split("/")[2]}/person/${person.label}`)}
                                /> 
                            )
                        })
                    }
                </Suspense>
            </div>
        </div>
    )
}