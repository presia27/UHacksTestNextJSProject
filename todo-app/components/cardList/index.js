'use client'

import CardComponent from "../cardComponent";
import { useState, useEffect } from "react";

const CardList = () => {
    const [todoList, setTodoList] = useState([]);
    
    useEffect(() => {
        
    }, [])

    return (
        <div>
            <CardComponent name="test" priority="test" />
            <CardComponent name="test" priority="test" />
        </div>
    )
}

export default CardList;