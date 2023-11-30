import TopNav from "./TopNav";
import LeftNav from "./LeftNav";
import Content from "./Content";

function Home() {
  return(
    <div className="flex">
    <LeftNav />
    <div className="flex-1">
      <TopNav />
      <div className="mt-4">
        <Content />
      </div>
    </div>
  </div>
  )
}

export default Home