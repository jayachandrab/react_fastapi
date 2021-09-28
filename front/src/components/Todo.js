import axios from "axios";
import React from "react";

function SearchProfile(props){
 
    return (
        <div>
            <p>
            <span style={{fontWeight:'bold,underline'}}>
            {props.todo.name}
            </span>
           
            

            </p>
        </div>
    )
}

export default SearchProfile;