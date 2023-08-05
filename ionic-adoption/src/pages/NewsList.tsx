import {
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonCardTitle,
    IonContent,
    IonHeader,
    IonTitle,
    IonToolbar,
    IonModal,
    IonButton,
    IonIcon,
    useIonRouter,
} from "@ionic/react";
import React from "react";
import { logOutOutline } from "ionicons/icons";
import { BASE } from "../constants";

const NewsList: React.FC = () => {
    const router = useIonRouter();
    const doLogout = () => {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ refresh: localStorage.getItem("refresh") }),
        };

        // There is no await here because I don't care about the result.
        fetch(`${BASE}/token/blacklist/`, requestOptions);

        localStorage.setItem("token", "");
        localStorage.setItem("refresh", "");
        router.push("/", "root", "replace");
    };

    // Declare a state variable to store the posts data
    const [posts, setPosts] = React.useState([]);

    // Define a function to fetch the posts data
    async function getNews() {
        const token = localStorage.getItem("token");
        const requestOptions = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
        };

        const response = await fetch(`${BASE}/news/`, requestOptions);

        const data = await response.json();

        // console.log(data);

        setPosts(data);
    }

    React.useEffect(() => {
        getNews();
    }, []);

    function createImg(post_animal) {
        if (post_animal && post_animal.image) {
            return (
                <IonCardContent>
                    <img width="100" height="100" src={post_animal.image} />
                </IonCardContent>
            );
        }

        return "";
    }

    return (
        <IonContent>
            <IonHeader>
                <IonToolbar>
                    <IonTitle>News Feed</IonTitle>
                    <IonButton type="submit" onClick={doLogout} slot="end">
                        Logout{" "}
                        <IonIcon slot="end" icon={logOutOutline}></IonIcon>
                    </IonButton>
                </IonToolbar>
            </IonHeader>
            {posts.map((post, index) => (
                <IonCard id={index + "post"}>
                    <IonCardHeader>
                        <IonCardTitle>{post.title}</IonCardTitle>
                    </IonCardHeader>
                    <IonCardContent>
                        <p>
                            {post.body.length > 25
                                ? `${post.body.slice(0, 25)}...`
                                : post.body}
                        </p>
                    </IonCardContent>
                    <IonModal trigger={index + "post"}>
                        <IonHeader>
                            <IonToolbar>
                                <IonTitle>{post.title}</IonTitle>
                            </IonToolbar>
                        </IonHeader>
                        <IonContent className="ion-padding">
                            <p>
                                {post.author
                                    ? `By: ${post.author.username}`
                                    : ""}
                            </p>
                            <p>
                                Posted on: {post.date_created.substring(0, 10)}
                            </p>
                            <p>{post.body}</p>
                            {createImg(post.animal)}
                        </IonContent>
                    </IonModal>
                </IonCard>
            ))}
        </IonContent>
    );
};

export default NewsList;
