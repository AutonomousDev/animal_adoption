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
} from "@ionic/react";
import React from "react";

const NewsList: React.FC = () => {
    return (
        <IonContent>
            <IonCard>
                <IonCardHeader>
                    <IonCardTitle>New Cat</IonCardTitle>
                    <IonCardSubtitle>Placeholder cat</IonCardSubtitle>
                </IonCardHeader>

                <IonCardContent>
                    <img
                        alt="Silhouette of mountains"
                        src="https://placekitten.com/100/100"
                    />
                </IonCardContent>
                <IonCardContent>A cat.</IonCardContent>
            </IonCard>
        </IonContent>
    );
};

export default NewsList;
