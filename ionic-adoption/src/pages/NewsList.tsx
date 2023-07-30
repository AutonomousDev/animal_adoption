import {
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonCardTitle,
    IonContent,
    IonButton,
    IonIcon,
    IonGrid,
    IonRow,
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
            <IonGrid>
                <IonRow class="ion-justify-content-end">
                    <IonButton
                        className="ion-margin-top"
                        type="submit"
                        onClick={doLogout}
                    >
                        Logout{" "}
                        <IonIcon slot="end" icon={logOutOutline}></IonIcon>
                    </IonButton>
                </IonRow>
                <IonRow></IonRow>
            </IonGrid>
            {posts.map((post) => (
                <IonCard>
                    <IonCardHeader>
                        <IonCardTitle>{post.title}</IonCardTitle>
                        {/* <IonCardSubtitle></IonCardSubtitle> */}
                    </IonCardHeader>
                    {createImg(post.animal)}

                    <IonCardContent>
                        <p>
                            {post.author ? `By: ${post.author.username}` : ""}
                        </p>
                        <p>{post.body}</p>
                    </IonCardContent>
                </IonCard>
            ))}
        </IonContent>
    );
};

export default NewsList;
