//
//  SwiftUIView.swift
//  Food_Inc
//
//  Created by Andrew Thomas on 7/8/20.
//  Copyright © 2020 Food Inc. All rights reserved.
//

import SwiftUI
import FirebaseFirestore

var db: Firestore!

func getAllRestaurants() {
    db = Firestore.firestore()
    db.collection("Restaurants").getDocuments() { (querySnapshot, err) in
        if let err = err {
            print("Error: \(err)")
        } else {
            for restaurant in querySnapshot!.documents {
                print("\(restaurant.documentID) => \(restaurant.data())")
            }
        }
    }
}

