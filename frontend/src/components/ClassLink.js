export function ClassLink(props) {
    return (
        <h5><a href="#" onClick={() => props.setCode(props.code)}>{props.code}</a> - {props.name}</h5>
    );
}