import {ClassLink} from './ClassLink';

export default function Unlocks(props) {
    if (props.unlocks) {
        const classLinks = [];
        for (const unlock of props.unlocks) {
            classLinks.push(<ClassLink code={unlock.code} name={unlock.name} setCode={props.setCode}/>)
        }
        return (
            <div>
                <h3>Unlocks</h3>
                {classLinks}
            </div>
        );
    }
    return <div></div>
}