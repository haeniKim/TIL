## React.js

> [React] 공식문서

# [React] Describing the UI

# [Describing the UI](https://react.dev/learn/describing-the-ui)

---

> React는 사용자 인터페이스(UI)를 렌더링하기 위한 JavaScript 라이브러리
> 
- 배울 내용 : React 컴포넌트 생성, 사용자 정의, 조건부 표시
- UI → 버튼, 텍스트, 이미지와 같은 작은 단위로 구성
- React를 사용하면 재사용 가능, 중첩 가능한 컴포넌트로 결합 가능

## 1. Your First Component

### *Component*

- markup으로 사용할 수 있는 JavaScript 함수
- React application은 컴포넌트들로 구축되어짐.
- button과 같은 작은 것일 수도 있고, 전체 페이지일 수도 있음.
- 재사용 가능한 UI 구성 요소
- HTML 태그와 마찬가지로 컴포넌트를 작성하고, 순서를 정하고 중첩해서 전체 페이지를 디자인할 수 있음

### 1) Define Component

> 기존에는 웹 페이지를 만들 때 콘텐츠를 마크업하고 JS를 사용해 상호 작용을 추가했음. React를 사용하면 같은 기술을 사용하면서도 상호작용을 우선시 함.
> 
- React component는 마크업으로 뿌릴 수 있는 JavaScript 함수

### 2) How to build a Component

    **Step 1: Export the component**

`export default` - 표준 JS 구문

    **Step 2: Define the function**

`function 함수명() {}` 

    **Step 3: Add markup**

### 3) Using a component

- 다른 컴포넌트에 중첩하여 사용 가능

```jsx
function Profile() {
  return (
    <img
      src="https://i.imgur.com/MK3eW3As.jpg"
      alt="Katherine Johnson"
    />
  );
}

export default function Gallery() {
  return (
    <section>
      <h1>Amazing scientists</h1>
      <Profile />
      <Profile />
      <Profile />
    </section>
  );
}
```

### 4) What the browser sees (브라우저에 표시되는 내용)

- 대소문자 차이에 주목
- 보통 소문자 태그는 HTML 태그
- 보통 대문자 태그는 컴포넌트

### 5) Nesting and organizing componets (컴포넌트 중첩 및 구성)

- 같은 파일에 여러 컴포넌트 포함, 및 분리 가능
- 한 번 정의 해놓고 필요할 때 마다 재사용 가능

### Summary

- React lets you create components, **reusable UI elements for your app.**
- In a React app, every piece of UI is a component.
- React components are regular JavaScript functions except:
    1. Their names always begin with a **capital letter.**
    2. They return JSX markup.

## 2. Importing and Exporting Componets

> 하나의 파일에 여러 컴포넌트를 선언할 수 있지만, 파일이 큰 경우 탐색이 어려우므로 컴포넌트를 자제 파일로 export 해서 다른 파일에서 컴포넌트를 import 하여 사용 가능
> 
- component를 조합해 또 다른 component 생성 가능
- 여러번 중첩하게 될 경우, 파일 분리를 통해 편의성을 높일 수 있음.

### 1) The root component file

```jsx
function Profile() {
  return (
    <img
      src="https://i.imgur.com/MK3eW3As.jpg"
      alt="Katherine Johnson"
    />
  );
}

export default function Gallery() {
  return (
    <section>
      <h1>Amazing scientists</h1>
      <Profile />
      <Profile />
      <Profile />
    </section>
  );
}
```

위의 코드에서 `Profile`  , `Gallery`  컴포넌트는 모두 `Apps.js`  root componet 파일에 존재.

- Create React App에서는 앱 전체가 `src/App.js` 에서 실행

### 2) Exporting and importing a component

- 컴포넌트 분리를 통해 모듈성 강화 및, 다른 파일에서 재사용 용이하게 할 수 있음

<aside>
👉 **[ 컴포넌트 분리 ]**

  1. Make a new JS file to put the components in.

  2. Export your function component from that file (using dafault, named export)

  3. Import it in the file where you’ll use the component (using the corresponding technique for importing [default](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/import#importing_defaults) or [named](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/import#import_a_single_export_from_a_module) exports).

</aside>

**App.js**

```jsx
import Gallery from "./component/Gallery";

export default function App() {
  return (
    <Gallery />
  );
}
```

**Gallery.js**

```jsx
function Profile() {
    return (
      <img
        src="https://i.imgur.com/QIrZWGIs.jpg"
        alt="Alan L. Hart"
      />
    );
  }
  
  export default function Gallery() {
    return (
      <section>
        <h1>Amazing scientists</h1>
        <Profile />
        <Profile />
        <Profile />
      </section>
    );
  }
```

1. `Gallery.js`:
    - Defines the `Profile` component which is only used within the same file and is not exported.
    - Exports the `Gallery` component as a **default export.**
2. `App.js`:
    - Imports `Gallery` as a **default import** from `Gallery.js`.
    - Exports the root `App` component as a **default export.**

### 3) **Exporting and importing multiple components from the same file**

- 하나의 파일은 하나의 default export만 가질 수 있음.
- 하나의 파일에서 여러 컴포넌트 사용을 위해서는
    
    1) 새 파일을 만들어 default export 하거나, 
    
    2) named export를 추가
    

**named export**

```jsx
export function Profile() {
  // ...
}
```

```jsx
import { Profile } from './Gallery.js';
```

- 중괄호를 사용해 import 할 수 있음

### Summary

On this page you learned:

- What a root component file is
- How to import and export a component
- When and how to use default and named imports and exports
- How to export multiple components from the same file

## 3. Writing Markup with JSX

### JSX

- React Component는 JSX라는 구문 확장자를 사용해 마크업을 표현
- HTML과 비슷하지만 더 엄격하고, 동적인 정보를 표시할 수 있음
- JavaScript를 확장한 문법으로, JavaScript 파일 안에 HTML과 유사한 마크업을 작성할 수 있게 해줌

### 1) JSX: Putting markup into JavaScript

> 보통 웹을 만들 때 HTML⇒ 컨텐츠, CSS ⇒ 디자인, JavaScript ⇒ 로직. but interactive 해지면서 로직이 컨텐츠를 결정하는 경우가 많아져 렌더링 로직과 마크업이 같은 위치의 컴포넌트에 있게 됨.
> 

### 2) Converting HTML to JSX / The Rules of JSX

**1. Return a single root element**

- 컴포넌트에서 여러 엘리먼트를 반환할 때 하나의 부모 태그로 감싸야 함
- ex) <div></div> , <>, </>
- `<>, </>` - fragment, 브라우저상 HTML 트리 구조에서 흔적을 남기지 않고 그룹화해줌

> **JSX태그를 하나로 감싸는 이유?**
⇒ JSX는 HTML처럼 보이지만 내부적으로 JS 객체로 변환되기 때문에 하나의 배열로 감싸야 함.
> 

**2. Close all the tags**

- 모든 태그를 닫는 태그로 사용해야 함
- ex) `<img>`  ⇒ `<img />`

**3. camelCase ~~all~~ most of the things!**

- 변수명에 대시나 예약어 사용 불가

### 3) JSX 변환기 사용

[HTML to JSX](https://transform.tools/html-to-jsx)

### Summary

Now you know why JSX exists and how to use it in components:

- React components group rendering logic together with markup because they are related.
- JSX is similar to HTML, with a few differences. You can use a [converter](https://transform.tools/html-to-jsx) if you need to.
- Error messages will often point you in the right direction to fixing your markup.

## 4. JavaScript in JSX with Curly Braces

> JSX를 사용하면 JS 파일 내에 HTML과 유사한 마크업 언어를 작성해 rendering logic과 content를 같은 위치에 둘 수 있음. JSX에서 중괄호를 사용해 마크업 안에 JavaScript 로직을 추가하거나 동적인 property를 참고할 수 있음.
> 

### 1) Passing strings with quotes(””, ‘’)

- JSX에 문자열 속성을 전달하려면, 작은 따옴표 혹은 큰 따옴표로 묶음

```jsx
export default function Avatar() {
  return (
    <img
      className="avatar"
      src="https://i.imgur.com/7vQD0fPs.jpg"
      alt="Gregorio Y. Zara"
    />
  );
}
```

- `{}`  : `" "` 대신 사용. 동적으로 지정해 JS 값 사용 가능

### 2) Using curly braces / 중괄호 사용 위치

- `{}`  중괄호 사이에는 함수 호출을 포함한 모든 JS 표현식이 작동

**1. JSX 태그 안에 직접 텍스트로 사용**

`<h1>{name}'s To Do List</h1>` ⇒ O

`<{tag}>Gregorio Y. Zara's To Do List</{tag}>` ⇒ X

**2. `=` 기호 바로 뒤에 오는 속성**

`src={avatar}` ⇒ 아바타 변수

`src="{avatar}"` ⇒ 문자열 “{avatar}”

### 3) Using “double curlies”: CSS and other objects in JSX

- `{{ }}` - JSX에서 JS 객체 전달, JSX 중괄호 내부의 객체
- ex) 인라인 스타일이 필요한 경우 style attribute에 객체 전달 `style={{ }}`

```jsx
export default function TodoList() {
  return (
    <ul style={{
      backgroundColor: 'black',
      color: 'pink'
    }}>
      <li>Improve the videophone</li>
      <li>Prepare aeronautics lectures</li>
      <li>Work on the alcohol-fuelled engine</li>
    </ul>
  );
}
```

### 4) **More fun with JavaScript objects and curly braces**

- 여러 표현식을 하나의 객체로 이동해 중괄호 안에 있는 JSX에서 참조할 수 있음

```jsx
const person = {
  name: 'Gregorio Y. Zara',
  theme: {
    backgroundColor: 'black',
    color: 'pink'
  }
};

export default function TodoList() {
  return (
    <div style={person.theme}>
      <h1>{person.name}'s Todos</h1>
      <img
        className="avatar"
        src="https://i.imgur.com/7vQD0fPs.jpg"
        alt="Gregorio Y. Zara"
      />
      <ul>
        <li>Improve the videophone</li>
        <li>Prepare aeronautics lectures</li>
        <li>Work on the alcohol-fuelled engine</li>
      </ul>
    </div>
  );
```

### Summary

Now you know almost everything about JSX:

- JSX attributes inside quotes are passed as strings.
- Curly braces let you bring JavaScript logic and variables into your markup.
- They work inside the JSX tag content or immediately after `=` in attributes.
- `{{` and `}}` is not special syntax: it’s a JavaScript object tucked inside JSX curly braces.
- 따옴표 안의 JSX 속성은 문자열로 전달됩니다.
- 중괄호를 사용하면 JavaScript 로직과 변수를 마크업으로 가져올 수 있습니다.
- 중괄호는 JSX 태그 콘텐츠 내부 또는 속성의 `=` 바로 뒤에서 작동합니다.
- `{{` 와 `}}` 는 특별한 구문이 아니라 JSX 중괄호 안에 들어 있는 JavaScript 객체입니다.

## 5. Passing Props to a Component

### 1) Props

- component 간 통신을 위해 사용
- 부모 component는 자식 component에 props를 전달해 정보를 줄 수 있음
- HTML attributes, 객체, 배열, 함수, JSX를 포함한 JavaScript 값 전달 가능
- JSX 태그에 전달하는 정보
    - ex) `className`, `src`, `alt`, `width`, `height` 는 `<img>` 태그에 전달, 그 외 어떤 컴포넌트에도 props 전달 가능

### 2) Passing props to a component/ Step

**Step 1: Pass props to the child component (자식 컴포넌트에 props 전달)**

```jsx
export default function Profile() {
  return (
    <Avatar
      person={{ name: 'Lin Lanying', imageId: '1bX5QH6' }}
      size={100}
    />
  );
}
```

**Step 2: Read props inside the child component (자식 컴포넌트 내부에서 props 읽기)**

```jsx
function Avatar({ person, size }) {
  // person and size are available here
}
```

🚨 props 선언 시 `()` 안에 `{ }` 잊지 않기

### 3) Props - default value

- 변수 뒤에 `= 기본값`
    
    ```jsx
    function Avatar({ person, size = 100 }) {
      // ...
    }
    ```
    
- prop이 없거나 undefined인 경우 ( null, 0인 경우는 X)

### 4) JSX spread syntax

- 모든 props를 한번에 전달

```jsx
function Profile({ person, size, isSepia, thickBorder }) {
  return (
    <div className="card">
      <Avatar
        person={person}
        size={size}
        isSepia={isSepia}
        thickBorder={thickBorder}
      />
    </div>
  );
}
```

```jsx
function Profile(props) {
  return (
    <div className="card">
      <Avatar {...props} />
    </div>
  );
}
```

### 5) component 중첩

```jsx
<Card>
	<Avatar />
</Card>
```

- JSX 태그 내 콘텐츠 중첩을 하면 부모 컴포넌트는 해당 컨텐츠를 `children` 이라는 prop으로 받음

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/02e0792b-c475-4c1b-9192-9bff7c1fa4a3/410d8866-7252-45df-a6a0-b79b52e7cf26/Untitled.png)

### Summary

- To pass props, add them to the JSX, just like you would with HTML attributes.
- To read props, use the `function Avatar({ person, size })` destructuring syntax.
- You can specify a default value like `size = 100`, which is used for missing and `undefined` props
- You can forward all props with `<Avatar {...props} />` JSX spread syntax, but don’t overuse it!
- Nested JSX like `<Card><Avatar /></Card>` will appear as `Card` component’s `children` prop.
- Props are read-only snapshots in time: every render receives a new version of props.
- You can’t change props. When you need interactivity, you’ll need to set state.
    - Props는 변경할 수 없습니다. 상호작용이 필요한 경우 state를 설정해야 합니다.

## 6. Conditional Rendering

> `if문` , `&&` , `? :` 와 같은 JavaScript 구문을 사용해 조건부로 JSX를 렌더링할 수 있음.
> 

### 1) If / else 를 사용한 조건부 렌더링

```jsx
if (isPacked) {
  return <li className="item">{name} ✔</li>;
}
return <li className="item">{name}</li>;
```

- 아무 것도 반환하지 않을 때 `null` 사용
    - `return null;`

### 2) Conditional(ternary) operator (`? :`  ) - 삼항연산자

```jsx
if (isPacked) {
  return <li className="item">{name} ✔</li>;
}
return <li className="item">{name}</li>;
```

```jsx
return (
  <li className="item">
    {isPacked ? name + ' ✔' : name}
  </li>
);
```

- `con ? A : B` ⇒ condition 이 true이면 A 렌더링, false이면 B 렌더링

### 3) 논리 AND 연산자 (`&&`)

```jsx
return (
  <li className="item">
    {name} {isPacked && '✔'}
  </li>
);
```

- 조건이 참일 때 렌더링, 그렇지 않으면(false), 아무 것도 렌더링 하지 않음

### Summary

- In React, you control branching logic with JavaScript.
- You can return a JSX expression conditionally with an `if` statement.
- You can conditionally save some JSX to a variable and then include it inside other JSX by using the curly braces.
- In JSX, `{cond ? <A /> : <B />}` means *“if `cond`, render `<A />`, otherwise `<B />`”*.
- In JSX, `{cond && <A />}` means *“if `cond`, render `<A />`, otherwise nothing”*.
- The shortcuts are common, but you don’t have to use them if you prefer plain `if`.

## 7. Rendering Lists

> JavaScript의 `filter()` , `map()` 을 사용해 데이터 배열을 필터링하고 component의 배열로 변환할 수 있음. 각 배열 항목마다 `key` 를 지정해 목록이 변경되더라도 목록에서 각 항목의 위치 추적 가능
> 

### 1) Rendering data from arrays

1. Move the data into an array
    
    ```jsx
    const people = [
      'Creola Katherine Johnson: mathematician',
      'Mario José Molina-Pasquel Henríquez: chemist',
      'Mohammad Abdus Salam: physicist',
      'Percy Lavon Julian: chemist',
      'Subrahmanyan Chandrasekhar: astrophysicist'
    ];
    ```
    
2. Map the data into a new array of JSX nodes
    
    ```jsx
    const listItems = people.map(person => <li>{person}</li>);
    ```
    
3. Return new array from the component 
    
    ```jsx
    return <ul>{listItems}</ul>;
    ```
    

### 2) Filtering arrays of items

1. Create a new array of some conditions, by calling `filter()` on the array filtering by conditions.
    
    ```jsx
    const chemists = people.filter(person =>
      person.profession === 'chemist'
    );
    ```
    
2. map over new array
    
    ```jsx
    const listItems = chemists.map(person =>
      <li>
         <img
           src={getImageUrl(person)}
           alt={person.name}
         />
         <p>
           <b>{person.name}:</b>
           {' ' + person.profession + ' '}
           known for {person.accomplishment}
         </p>
      </li>
    );
    ```
    
3. return the mapped array from the component
    
    ```jsx
    return <ul>{listItems}</ul>;
    ```
    
    <aside>
    👉 화살표 함수(`⇒`)는 바로 뒤에 표현식을 암시적으로 Reurn하므로 `return` 문이 필요하지 않음.
    하지만 중괄호(`{}`)가 오는 경우는 `return` 문 필요.
    
    </aside>
    

### 3) About `key`

- map각 배열의 항목들을 고유하게 식별할 수 있는 문자열 또는 숫자인 key를 부여해야 함.
- key는 각 컴포넌트가 어떤 배열 항목에 해당하는지 알려줘 매칭하도록 함.
- 따로 지정하지 않으면 기본적으로 Index를 Key로 사용하지만 새 항목 삽입, 삭제, 배열 순서가 바뀌면서 변경될 수 있음

**key를 얻는 방법**

1. Database 데이터 : 고유한 DB key/ID 사용 
2. Local 데이터 : incrementing counter, `crypto.randomUUID()` , `uuid` 패키지 사용

**key 규칙**

- 같은 배열 JSX 노드에는 고유해야 함.
- Key는 변경되지 않아야 함 (렌더링 중 생성 금지)

### Summary

- How to move data out of components and into data structures like arrays and objects.
- How to generate sets of similar components with JavaScript’s `map()`.
- How to create arrays of filtered items with JavaScript’s `filter()`.
- Why and how to set `key` on each component in a collection so React can keep track of each of them even if their position or data changes.

## 8. Keeping Components Pure

### Pure function

1. 자신의 일만 처리 - 호출 전 존재했던 객체나 변수를 변경하지 않음
2. same inputs, same outputs - 동일 입력에는 항상 동일 결과 반환
- 버그나 예측 불가한 동작이 발생하는 것을 피할 수 있음.

### 1) **Purity: Components as formulas**

- React는 모든 컴포넌트가 pure function 이라고 가정.

### 2) **Side Effects: (un)intended consequences**

- 컴포넌트는 JSX만을 반환해야 하고, 렌더링 전 존재하는 객체, 변수를 변경해서는 안됨

[순수성을 어기는 예시]

```jsx
let guest = 0;

function Cup() {
  // Bad: changing a preexisting variable!
  // 나쁨: 기존 변수를 변경합니다!
  guest = guest + 1;
  return <h2>Tea cup for guest #{guest}</h2>;
}

export default function TeaSet() {
  return (
    <>
      <Cup />
      <Cup />
      <Cup />
    </>
  );
}
```

[수정]

```jsx
function Cup({ guest }) {
  return <h2>Tea cup for guest #{guest}</h2>;
}

export default function TeaSet() {
  return (
    <>
      <Cup guest={1} />
      <Cup guest={2} />
      <Cup guest={3} />
    </>
  );
}
```

### 3) **Local mutation: Your component’s little secret**

- 렌더링 전에 존재하는 것을 변경하는 것은 안되지만 렌더링 하는 동안 ‘방금’ 생성한 변수와 객체를 변경하는 것은 가능
    
    ```jsx
    function Cup({ guest }) {
      return <h2>Tea cup for guest #{guest}</h2>;
    }
    
    export default function TeaGathering() {
      let cups = [];
      for (let i = 1; i <= 12; i++) {
        cups.push(<Cup key={i} guest={i} />);
      }
      return cups;
    }
    ```
    

### 4) **Where you *can* cause side effects**

- 화면 업데이트, 애니메이션 시작, 데이터 변경과 같은 변경을 side effect라고 함. **렌더링 중이 아닌 ‘부수적으로’** 일어나는 일

**event handler**

- 대게 React에서 사이트 이펙트는 event handler에 속함
- 사용자가 어떤 동작 수행할 때, React가 실행하는 함수
- 컴포넌트 내부에 정의되어 있지만 렌더링 중에는 실행되지 않음
- 적절한 event handler가 없다면 `useEffect` 사용

### Summary

- A component must be pure, meaning:
    - **It minds its own business.** It should not change any objects or variables that existed before rendering.
    - **Same inputs, same output.** Given the same inputs, a component should always return the same JSX.
- Rendering can happen at any time, so components should ***not depend on each others’ rendering sequence.***
- You should not mutate any of the inputs that your components use for rendering. That includes props, state, and context. To update the screen, [“set” state](https://react-ko.dev/learn/state-a-components-memory) instead of mutating preexisting objects.
- Strive to express your component’s logic in the JSX you return. When you need to “change things”, you’ll usually want to do it in an event handler. As a last resort, you can `useEffect`.
- Writing pure functions takes a bit of practice, but it unlocks the power of React’s paradigm.