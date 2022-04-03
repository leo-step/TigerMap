import {ClassLink} from './ClassLink';

export default function Prereqs(props) {
    if (props.prereqs) {
        const classLinks = [];
        for (const prereq of props.prereqs) {
            classLinks.push(<ClassLink code={prereq.code} name={prereq.name} setCode={props.setCode}/>)
        }
        return (
            <div>
                <h3>Prereqs</h3>
                {classLinks}
            </div>
        );
    }
    return <div></div>
}