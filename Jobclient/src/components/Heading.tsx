import { ReactElement } from "react"
import '../index.css'

type HeadingProps = {title: string}

const Heading = ({title}: HeadingProps): ReactElement => {
    return <h1 className="custom-heading">{title}</h1>
}
export default Heading