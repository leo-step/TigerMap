import {useState} from 'react';
import banner from '../assets/banner.png'

export default function Footer() {
    return (
        <div style={{textAlign: "center", backgroundColor: "#fe8a07", fontWeight: 600}}>
            <img src={banner} style={{width: "100%"}}/>
            <p style={{paddingTop: "12px"}}>Built by Leo Stepanewk and Aaliyah Sayed, inspired by Kevin Wayne #cos226</p>
        </div>
    );
}