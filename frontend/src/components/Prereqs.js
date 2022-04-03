import {ClassLink} from './ClassLink';

export default function Prereqs(props) {
    if (props.prereqs) {
        const classLinks = [];
        let i = 0;
        for (const prereq of props.prereqs) {
            classLinks.push(<ClassLink key={i} code={prereq.code} name={prereq.name} setCode={props.setCode}/>)
            i++;
        }
        return (
            <div>
                <h3>Prereqs 🔒</h3>
                {classLinks}
            </div>
        );
    }
    return <div></div>
}