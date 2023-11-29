import Cookies from 'universal-cookie';
import { loginUser } from "../services/login";
import LoginForm from "../components/LoginForm";
import { useNavigate } from 'react-router-dom';


function Login() {

const cookies = new Cookies();
const navigate = useNavigate();
const setAuthToken = (authToken: string) => {
    cookies.set('authToken', authToken, { path: '/' });
    navigate('/', { replace: true });
};
// const getAuthToken = () => {cookies.get('authToken')};

const handleLogin = async (username: string, password: string) => {
    if (!username || !password){
      return
    }
    try {
      const token = await loginUser(username, password);
      // console.log('Token:', token);
      if (!token){console.error('No token'); return}
      setAuthToken(token);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
  return(
  <LoginForm onSubmit={handleLogin} />
  );
}

export default Login