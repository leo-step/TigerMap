import {useState, useEffect} from 'react';
import { Container, Row, Col } from 'reactstrap';
import ClassInfo from './ClassInfo';
import Prereqs from './Prereqs';
import SearchBar from './SearchBar';
import Unlocks from './Unlocks';

export default function Main(props) {
    const [code, setCode] = useState(null);
    
    useEffect(() => {
      if (code) {
        fetch("http://localhost:5000/api", {
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
      <Container style={{paddingTop: "16px"}}>
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
    );
  }