import Style from './cardComponent.module.css'

const CardComponent = ({name, priority}) => {
    return(
        <div className={Style.card}>
            <div><input type="checkbox" /></div>
            <div>{name}</div>
            <div>{priority}</div>
        </div>
    )
}

export default CardComponent;