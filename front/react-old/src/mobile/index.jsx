import React, {Component} from 'react';
import './mobile.css';
import Navbar from './components/navbar';

class IndexMobile extends Component{

    render(){
        return(
            <div>
                <Navbar/>
                <div className="mobile-container">
                    <h1>INDEX MOBILE</h1>
                </div>

                
            </div>
        );
    }
}

export default IndexMobile;