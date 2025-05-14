import CardComponent from "@/components/cardComponent";

const Main = () => {
    return(
        <main>
            <section>
                <div>
                    <h1>TO-DO APP</h1>
                </div>
            </section>

            <section>
                <div>
                    wrapper
                    <div>
                        cards go here
                        <CardComponent />
                    </div>
                </div>
            </section>
        </main>
        
    )
}



export default Main;
