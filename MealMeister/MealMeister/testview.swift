//
//  testview.swift
//  MealMeister
//
//  Created by Brett Beattie on 7/30/20.
//  Copyright © 2020 Andrew Thomas. All rights reserved.
//
import SwiftUI
import UIKit
import Firebase

class ViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    
    @IBOutlet private weak var segmentControl: UISegmentedControl!
    @IBOutlet private weak var tableView: UITableView!
    
    private var restaurants = [Restaurant]()
    private var db = Firestore.firestore().collection("Restaurants")
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.delegate = self
        tableView.dataSource = self
        tableView.estimatedRowHeight = 80
        tableView.rowHeight = UITableView.automaticDimension
    }
    
    override func viewWillAppear(_ animated: Bool) {
        db.getDocuments { (snapshot, error) in
            if let err = error {
                debugPrint("Error fetching docs: \(err)")
            } else {
                guard let snap = snapshot else { return }
                for document in snap.documents {
                    let data = document.data()
                    
                    let displayName = data["Display_Name"] as? String ?? ""
                    let name = data["name"] as? String ?? ""
                    let tags = data["tags"] as? String ?? ""
                    
                    let restaurant = Restaurant(displayName: displayName, name: name, tag: tags)
                    self.restaurants.append(restaurant)
                }
                self.tableView.reloadData()
            }
        }
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return restaurants.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        if let cell = tableView.dequeueReusableCell(withIdentifier: "restaurantCell", for: indexPath) as? RestaurantCell {
            cell.configureCell(restaurant: restaurants[indexPath.row])
            return cell
        } else {
            return UITableViewCell()
        }
    }
}
