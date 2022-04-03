export default function ClassInfo(props) {
    if (props.course) {
        return (
            <div>
                <h2>{props.course.code} - {props.course.name}</h2>
                <p>{props.course.description}</p>
                <a href={props.course.link}>See more details</a>
            </div>
        );
    }
    return <div></div>
}