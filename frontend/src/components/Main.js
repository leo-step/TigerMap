import {useState, useEffect} from 'react';
import { Container, Row, Col } from 'reactstrap';
import ClassInfo from './ClassInfo';
import Prereqs from './Prereqs';
import SearchBar from './SearchBar';
import Unlocks from './Unlocks';
import Footer from './Footer';
import logo from '../assets/logo.png'

export default function Main(props) {
    const [code, setCode] = useState(null);
    
    useEffect(() => {
      if (code) {
        fetch("/api", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
          },
          body: JSON.stringify({"code": code}),
        })
        .then(response => response.json())
        .then(json => {
          props.setData(json);
        });
      }
    }, [code]);
  
    return (
      <div style={{display: "flex", "minHeight": "100vh", "flexDirection": "column", "justifyContent": "space-between"}}>
        <Container style={{paddingTop: "16px"}}>
          <Row className="justify-content-center" style={{textAlign: "center"}}>
            <img src={logo} style={{width: "500px"}}/>
            <h4 style={{paddingBottom: "16px"}}>A course selection treasure map 💎🗺️</h4>
          </Row>
          <Row className="justify-content-center">
            <Col style={{maxWidth: "500px"}}>
              <SearchBar setCode={setCode}/>
            </Col>
          </Row>
          <br />
          <Row>
            <Col>
              <ClassInfo course={props.data.course}/>
            </Col>
          </Row>
          <br />
          <Row>
            <Col>
              <Prereqs prereqs={props.data.prereqs} setCode={setCode}/>
            </Col>
            <Col>
                <Unlocks unlocks={props.data.unlocks} setCode={setCode}/>
            </Col>
          </Row>
        </Container>
        <br />
        <br />
        <Footer />
      </div>
    );
  }