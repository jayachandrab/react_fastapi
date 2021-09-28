import SearchProfile from './Todo'

function TodoView(props){
    return(
        <div>
            <ul>
                {props.todoList.map(todo=> <SearchProfile todo={todo} />)}
            </ul>
        </div>
    )
}

export default TodoView