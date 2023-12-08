import backgroundSVG from '../../assets/subtle-prism.svg'
import GenerateForm from "../../components/GenerateForm";
import Layout from "../Layout";


function Generate() {
    return (
    <Layout>
        <div className="space-x-1 shadow-xl rounded-xl text-center bg-blue-900/20 p-1 mt-4 flex-1 drop-shadow-xl justify-center items-center" style={{ backgroundImage: `url(${backgroundSVG})` }}>
            <GenerateForm />
        </div>
      </Layout>
    );
}

export default Generate;