import React, {Component} from 'react';
import './navbar.css';
import {Link} from 'react-router-dom';

class Navbar extends Component{

    render(){
        return(
            <header>
                <nav role="navigation">
                    <div id="menuToggle">
                        
                        <input type="checkbox" />
                        
                        {/*
                        Some spans to act as a hamburger.
                        
                        They are acting like a real hamburger,
                        not that McDonalds stuff.
                        */}
                        <span></span>
                        <span></span>
                        <span></span>
                        
                        {/*
                        Too bad the menu has to be inside of the button
                        but hey, it's pure CSS magic.
                        */}
                        <ul id="menu">
                            <Link to="/client/audio"><li>Audio</li></Link>
                            <Link to="/client/Mouse"><li>Mouse</li></Link>
                            <Link to="/client/Keyboard"><li>Keyboard</li></Link>
                            <Link to="/Video"><li>Video</li></Link>
                        </ul>
                    </div>
                    </nav>
            </header>
        );
    }
}

export default Navbar;
