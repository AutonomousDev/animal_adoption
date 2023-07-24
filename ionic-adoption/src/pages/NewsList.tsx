import {
    // IonAvatar,
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonContent,
    // IonHeader,
    // IonInfiniteScroll,
    // IonInfiniteScrollContent,
    // IonItem,
    // IonLabel,
    // IonList,
    // IonPage,
    // IonTitle,
    // IonToolbar,
    // useIonViewWillEnter,
} from "@ionic/react";
import React from "react";
import { BASE } from "../constants";

const NewsList: React.FC = () => {
    // Declare a state variable to store the posts data
    const [posts, setPosts] = React.useState([]);

    // Define a function to fetch the posts data
    async function getNews() {
        const token = localStorage.getItem("token");
        const requestOptions = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`,
            },
        };

        const response = await fetch(`${BASE}/news/`, requestOptions);

        const data = await response.json();

        setPosts(data);
    }

    React.useEffect(() => {
        getNews();
    }, []);

    // useIonViewWillEnter(() => {
    //     console.log("ionViewWillEnter event fired");
    // });

    return (
        <IonContent>
            {posts.map((post) => (
                <IonCard>
                    <IonCardHeader>
                        <IonCardTitle>{post.title}</IonCardTitle>
                        {/* <IonCardSubtitle></IonCardSubtitle> */}
                    </IonCardHeader>

                    <IonCardContent>
                        {/* <img
                            alt="Silhouette of mountains"
                            src="https://placekitten.com/100/100"
                        /> */}
                    </IonCardContent>
                    <IonCardContent>
                        <p>{post.author ? `By: ${post.author.username}` : ""}</p>
                        <p>{post.body}</p>
                    </IonCardContent>
                </IonCard>
            ))}
        </IonContent>
    );
};

export default NewsList;
