import React, { ReactNode } from 'react';
import LeftNav from "./LeftNav";
import TopNav from "./TopNav";

interface LayoutProps {
  children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="flex">
      <LeftNav />
      <div className="flex flex-col flex-1">
        <TopNav />
        <div className="mt-4 flex-1">{children}</div>
      </div>
    </div>
  );
};

export default Layout;