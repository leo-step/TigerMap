import {useState} from 'react';
import { Form, FormGroup, Input, Row, Col } from 'reactstrap';
import { SearchButton } from './SearchButton';

export default function SearchBar(props) {
    const [query, setQuery] = useState("");

    return (
        <Form onSubmit={(e) => e.preventDefault()}>
            <FormGroup>
                <Row>
                    <Col style={{paddingRight: "2px"}}>
                    <Input type="text" size="lg" value={query} placeholder="COS 226" 
                        onChange={(event) => setQuery(event.target.value.toUpperCase())}/>
                    </Col>
                    <Col md="auto" style={{paddingLeft: "2px"}}>
                        <SearchButton query={query} setCode={() => {props.setCode(query)}}/> 
                    </Col>
                </Row> 
            </FormGroup>        
        </Form>
    );
}