import { Button } from 'reactstrap';
import { GoSearch } from 'react-icons/go'

export function SearchButton(props) {
    let disabled = true;

    if (props.query.match(/^[A-Z][A-Z][A-Z] \d\d\d$/)) {
        disabled = false;
    }

    return (
        <Button type="submit" color="primary" size="lg" onClick={() => 
            {if (!disabled) props.setCode()}} disabled={disabled}><GoSearch />
        </Button>
    );
}