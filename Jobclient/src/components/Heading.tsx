import { ReactElement } from "react"
import '../index.css'


type HeadingProps = {
    title: string; 
    links: {text: string; url: string}[];
};


const Heading = ({title, links}: HeadingProps): ReactElement => {
    return (
        <div>
            <h1 className="custom-heading">{title}</h1>
            <ul className="custom-heading">
                {links.map((link, index) => (
                    <li key={index}>
                        <a href={link.url}>{link.text}</a>
                    </li>
                ))}
            </ul>
        </div>
    );
};
export default Heading