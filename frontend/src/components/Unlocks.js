import {ClassLink} from './ClassLink';

export default function Unlocks(props) {
    if (props.unlocks) {
        const classLinks = [];
        let i = 0;
        for (const unlock of props.unlocks) {
            classLinks.push(<ClassLink key={i} code={unlock.code} name={unlock.name} setCode={props.setCode}/>)
            i++;
        }
        return (
            <div>
                <h3>Unlocks 🔑</h3>
                {classLinks}
            </div>
        );
    }
    return <div></div>
}