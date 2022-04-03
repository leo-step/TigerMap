import {useState} from 'react';
import Main from './components/Main'

function App() {
  const [data, setData] = useState({"course": null, "prereqs": null, "unlocks": null});

  return (
    <Main data={data} setData={setData}/>
  );
}

export default App;
