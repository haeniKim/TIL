import { useState } from 'react';

export default function Counter() {
  const [number, setNumber] = useState(0);

  return (
    <>
      <h1>{number}</h1>
      <button onClick={() => {
        setNumber(number + 5);
        console.log("onClick : ", number)
      }}>+5</button>  
      {console.log(number)}
    </>
  )
}
