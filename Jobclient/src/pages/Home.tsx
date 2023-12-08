import Layout from "./Layout";
import Content from "./Content";
import jobutopialogo from "../assets/jobutopia-high-resolution-logo-black-transparent.svg"
import backgroundSVG from "../assets/subtle-prism.svg"

const Home: React.FC = () => {
  return (
    <Layout>
      <div className="flex items-center justify-center h-screen bg-cover bg-center" style={{ backgroundImage: `url(${backgroundSVG})` }}>
        <img
          className="max-w-1/6 max-h-24"
          src={jobutopialogo}
          alt="JobUtopia"
        />
      </div>
      <Content />
    </Layout>
  );
};

export default Home;