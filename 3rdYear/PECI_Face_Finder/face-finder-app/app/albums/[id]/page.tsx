'use client'

import AlbumOrganism from "@/app/components/organisms/album/AlbumOrganism";
import { usePathname } from "next/navigation";

export default function AlbumPage(){
    const pathName = usePathname()
    return (
        <AlbumOrganism albumId={pathName.split("/")[2]}/>
    );
}