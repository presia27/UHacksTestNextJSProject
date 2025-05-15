import CardComponent from "@/components/cardComponent";
import CardList from "@/components/cardList";
import PageStyle from "./page.module.css";

const Main = () => {
    let date = new Date();
    let nowDate = date.toLocaleDateString();

    return(
        <main>
            <section>
                <div className={PageStyle.mainHeader}>
                    <h1>TO-DO APP</h1>
                    <h2>{nowDate}</h2>
                </div>
            </section>

            <section>
                <div className={PageStyle.cardArea}>
                    <CardList />
                </div>
            </section>
        </main>
        
    )
}

export default Main;
