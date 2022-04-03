import {useState, useEffect} from 'react';
import { Container, Row, Col } from 'reactstrap';
import FullClass from './FullClass';
import Prereqs from './Prereqs';
import SearchBar from './SearchBar';
import Unlocks from './Unlocks';

export default function Main(props) {
    const [code, setCode] = useState(null);
    
    useEffect(() => {
      console.log(code);
      // fetch data using code
      //const data = null;
      //props.setData(null);
      // access data using props.data
    });
  
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
            <FullClass course={props.data.course}/>
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