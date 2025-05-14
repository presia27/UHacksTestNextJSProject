import Style from './cardComponent.module.css'

const CardComponent = () => {
    return(
        <div className={Style.card}>
            <div><input type="checkbox" /></div>
            <div>Name of task</div>
            <div>Priority</div>
        </div>
    )
}

export default CardComponent;